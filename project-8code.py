import numpy as np


class NumPyAnalyzer:

    total_sessions = 0
    _current_array = None


    @classmethod
    def get_array(cls):
        return cls._current_array

    @classmethod
    def set_array(cls, new_array):
        if isinstance(new_array, np.ndarray):
            cls._current_array = new_array
            return True
        return False

    @classmethod
    def print_array_info(cls):
        if cls._current_array is None:
            print("\nNo array loaded yet.")
            return

        arr = cls._current_array
        print("\n--- Current Active Array ---")
        print(
            f"Dimensions: {arr.ndim}D | Shape: {arr.shape} | Total Elements: {arr.size}"
        )
        print(arr)
        print("----------------------------")

    @classmethod
    def increment_sessions(cls):
        cls.total_sessions += 1

   
    @staticmethod
    def parse_floats(input_string):
        try:
            return [float(x) for x in input_string.strip().split()]
        except ValueError:
            return []

    @staticmethod
    def get_shape_from_user():
        print("\nSelect Array Dimension:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter choice (1-3): ").strip()

        try:
            if choice == "1":
                length = int(input("Enter length of array: "))
                if length > 0:
                    return (length,)
            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                if rows > 0 and cols > 0:
                    return (rows, cols)
            elif choice == "3":
                depth = int(input("Enter depth: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                if depth > 0 and rows > 0 and cols > 0:
                    return (depth, rows, cols)
        except ValueError:
            pass

        print("Invalid dimensions entered!")
        return None

    @staticmethod
    def parse_slice(slice_str, max_len):
        if not slice_str or ":" not in slice_str:
            return 0, max_len
        parts = slice_str.split(":")
        start = int(parts[0]) if parts[0].isdigit() else 0
        end = (
            int(parts[1])
            if len(parts) > 1 and parts[1].isdigit()
            else max_len
        )
        return start, end

    @staticmethod
    def create_array_menu():
        shape = NumPyAnalyzer.get_shape_from_user()
        if shape is None:
            return

        expected_size = 1
        for dim in shape:
            expected_size *= dim

        print(
            f"\nEnter exact {expected_size} numeric elements separated by spaces:"
        )
        elements = NumPyAnalyzer.parse_floats(input("Elements: "))

        if len(elements) != expected_size:
            print(
                f"Error: Expected {expected_size} numbers, but got {len(elements)}."
            )
            return

        arr = np.array(elements).reshape(shape)
        NumPyAnalyzer.set_array(arr)
        print("\nArray created successfully!")
        NumPyAnalyzer.print_array_info()

        if arr.ndim >= 2:
            while True:
                print("\n--- Indexing & Slicing Sub-Menu ---")
                print("1. Indexing (Retrieve single value)")
                print("2. Slicing (Extract range)")
                print("3. Go Back")
                sub_choice = input("Enter choice (1-3): ").strip()

                if sub_choice == "1":
                    try:
                        if arr.ndim == 2:
                            r = int(
                                input(
                                    f"Enter Row index (0 to {arr.shape[0]-1}): ")
                            )
                            c = int(
                                input(
                                    f"Enter Column index (0 to {arr.shape[1]-1}): "
                                )
                            )
                            print(
                                f"\n[Result] Value at ({r}, {c}): {arr[r, c]}"
                            )
                        elif arr.ndim == 3:
                            d = int(
                                input(
                                    f"Enter Depth index (0 to {arr.shape[0]-1}): "
                                )
                            )
                            r = int(
                                input(
                                    f"Enter Row index (0 to {arr.shape[1]-1}): "
                                )
                            )
                            c = int(
                                input(
                                    f"Enter Column index (0 to {arr.shape[2]-1}): "
                                )
                            )
                            print(
                                f"\n[Result] Value at ({d}, {r}, {c}): {arr[d, r, c]}"
                            )
                    except IndexError:
                        print("Index out of bounds!")
                    except ValueError:
                        print("Please enter valid integers.")

                elif sub_choice == "2":
                    try:
                        if arr.ndim == 2:
                            r_slice = input(
                                "Row slice (start:end or blank for all): "
                            ).strip()
                            c_slice = input(
                                "Column slice (start:end or blank for all): "
                            ).strip()

                            r_start, r_end = NumPyAnalyzer.parse_slice(
                                r_slice, arr.shape[0]
                            )
                            c_start, c_end = NumPyAnalyzer.parse_slice(
                                c_slice, arr.shape[1]
                            )

                            print("\n[Result] Sub-Array Slice:")
                            print(arr[r_start:r_end, c_start:c_end])

                        elif arr.ndim == 3:
                            d_slice = input(
                                "Depth slice (start:end): "
                            ).strip()
                            r_slice = input("Row slice (start:end): ").strip()
                            c_slice = input(
                                "Column slice (start:end): "
                            ).strip()

                            d_start, d_end = NumPyAnalyzer.parse_slice(
                                d_slice, arr.shape[0]
                            )
                            r_start, r_end = NumPyAnalyzer.parse_slice(
                                r_slice, arr.shape[1]
                            )
                            c_start, c_end = NumPyAnalyzer.parse_slice(
                                c_slice, arr.shape[2]
                            )

                            print("\n[Result] 3D Slice:")
                            print(
                                arr[
                                    d_start:d_end,
                                    r_start:r_end,
                                    c_start:c_end,
                                ]
                            )
                    except Exception:
                        print("Invalid slice format.")

                elif sub_choice == "3":
                    break

    @staticmethod
    def math_operations_menu():
        arr = NumPyAnalyzer.get_array()

        print("\n--- Mathematical Operations ---")
        print("1. Element-wise Addition")
        print("2. Element-wise Subtraction")
        print("3. Element-wise Multiplication")
        print("4. Element-wise Division")
        choice = input("Select Operation (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            print(
                f"\nEnter a secondary array with matching shape {arr.shape}:"
            )
            elements = NumPyAnalyzer.parse_floats(input("Elements: "))

            if len(elements) != arr.size:
                print(
                    f"Size mismatch! Need exactly {arr.size} elements."
                )
                return

            second_arr = np.array(elements).reshape(arr.shape)

            if choice == "1":
                print("\n[Result] Addition:\n", arr + second_arr)
            elif choice == "2":
                print("\n[Result] Subtraction:\n", arr - second_arr)
            elif choice == "3":
                print("\n[Result] Multiplication:\n", arr * second_arr)
            elif choice == "4":
                if 0 in second_arr:
                    print("Error: Division by zero!")
                    return
                print("\n[Result] Division:\n", arr / second_arr)

    @staticmethod
    def combine_split_menu():
        arr = NumPyAnalyzer.get_array()

        print("\n--- Combine or Split ---")
        print("1. Concatenate Arrays")
        print("2. Split Array")
        choice = input("Select choice (1-2): ").strip()

        if choice == "1":
            print(
                f"\nEnter a secondary array with total elements ({arr.size}):"
            )
            elements = NumPyAnalyzer.parse_floats(input("Elements: "))

            if len(elements) != arr.size:
                print("Element count does not match original array.")
                return

            second_arr = np.array(elements).reshape(arr.shape)
            axis = input(
                f"Enter Axis to concatenate along (0 to {arr.ndim-1}): "
            ).strip()

            if axis.isdigit() and 0 <= int(axis) < arr.ndim:
                res = np.concatenate((arr, second_arr), axis=int(axis))
                print("\n[Result] Concatenated Array:\n", res)
            else:
                print("Invalid axis.")

        elif choice == "2":
            axis = input(
                f"Enter Axis to split along (0 to {arr.ndim-1}): "
            ).strip()
            if not axis.isdigit() or not (0 <= int(axis) < arr.ndim):
                print("Invalid axis.")
                return

            axis = int(axis)
            dim_len = arr.shape[axis]
            parts = input(
                f"Enter number of equal parts to split (dimension length = {dim_len}): "
            ).strip()

            if parts.isdigit() and int(parts) > 0:
                num_parts = int(parts)
                if dim_len % num_parts == 0:
                    splits = np.split(arr, num_parts, axis=axis)
                    print(f"\n[Result] Split into {num_parts} parts:")
                    for i, sub_arr in enumerate(splits):
                        print(f"-- Part {i+1} --\n", sub_arr)
                else:
                    print(
                        f"Cannot divide length {dim_len} into {num_parts} equal parts."
                    )

    @staticmethod
    def search_sort_filter_menu():
        arr = NumPyAnalyzer.get_array()

        print("\n--- Search, Sort, or Filter ---")
        print("1. Search Target Value")
        print("2. Sort Array")
        print("3. Filter Array with Operator")
        choice = input("Select choice (1-3): ").strip()

        if choice == "1":
            val_str = input("Enter numeric value to search: ").strip()
            vals = NumPyAnalyzer.parse_floats(val_str)
            if vals:
                target = vals[0]
                indices = np.argwhere(arr == target)
                if indices.size > 0:
                    print(
                        f"\n[Result] Found {target} at coordinates:\n", indices
                    )
                else:
                    print(f"\n[Result] Value {target} not found.")

        elif choice == "2":
            print("1. Ascending\n2. Descending")
            order = input("Choice (1-2): ").strip()
            if order in ["1", "2"]:
                descending = order == "2"
                sorted_arr = np.sort(arr, axis=-1)
                if descending:
                    sorted_arr = np.flip(sorted_arr, axis=-1)
                print("\n[Result] Sorted Array:\n", sorted_arr)

        elif choice == "3":
            op = input("Enter operator (>, <, >=, <=, ==): ").strip()
            val_str = input("Enter threshold number: ").strip()
            vals = NumPyAnalyzer.parse_floats(val_str)

            if vals and op in [">", "<", ">=", "<=", "=="]:
                thresh = vals[0]
                if op == ">":
                    mask = arr > thresh
                elif op == "<":
                    mask = arr < thresh
                elif op == ">=":
                    mask = arr >= thresh
                elif op == "<=":
                    mask = arr <= thresh
                elif op == "==":
                    mask = arr == thresh

                print("\n[Result] Boolean Mask:\n", mask)
                print("\n[Result] Filtered Values:\n", arr[mask])

    @staticmethod
    def stats_menu():
        arr = NumPyAnalyzer.get_array()

        print("\n=============================================")
        print("       STATISTICAL DASHBOARD                 ")
        print("=============================================")
        print(arr)
        print("---------------------------------------------")
        print(f"Sum                : {np.sum(arr)}")
        print(f"Mean               : {np.mean(arr):.4f}")
        print(f"Median             : {np.median(arr):.4f}")
        print(f"Std Dev            : {np.std(arr):.4f}")
        print(f"Variance           : {np.var(arr):.4f}")
        print(f"Min                : {np.min(arr)}")
        print(f"Max                : {np.max(arr)}")
        print("---------------------------------------------")

        p_str = input("\nEnter Percentile rank (0 - 100): ").strip()
        p_vals = NumPyAnalyzer.parse_floats(p_str)
        if p_vals and 0 <= p_vals[0] <= 100:
            print(
                f"[Result] {p_vals[0]}th Percentile: {np.percentile(arr, p_vals[0]):.4f}"
            )

        print(
            f"\nEnter secondary dataset of size {arr.size} for Correlation:"
        )
        corr_elements = NumPyAnalyzer.parse_floats(input("Elements: "))
        if len(corr_elements) == arr.size:
            corr_matrix = np.corrcoef(arr.flatten(), np.array(corr_elements))
            print("\n[Result] Correlation Matrix:\n", corr_matrix)

    @classmethod
    def main(cls):
        cls.increment_sessions()

        while True:
            print("\nWelcome to the NumPy Analyzer!")
            print("===================================")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                cls.create_array_menu()

            elif choice in ["2", "3", "4", "5"]:
                if cls.get_array() is None:
                    print("\n[!] Please create an array first using option 1.")
                else:
                    if choice == "2":
                        cls.math_operations_menu()
                    elif choice == "3":
                        cls.combine_split_menu()
                    elif choice == "4":
                        cls.search_sort_filter_menu()
                    elif choice == "5":
                        cls.stats_menu()

            elif choice == "6":
                print(
                    "Thank you for using the NumPy Analyzer! Goodbye!"
                )
                break
            else:
                print(
                    "Invalid choice. Please enter a number between 1 and 6."
                )


if __name__ == "__main__":
    NumPyAnalyzer.main()
