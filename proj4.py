# Global variable
dataset_summary = {}
# Aa global variable che je program na badha functions ma use thai shake che

# ------------------------------
# INPUT FUNCTIONS
# ------------------------------
def input_1d():
    """Input 1D list manually"""
    # User pase thi space thi numbers levana
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    return data
    # Aa function list return kare che

def input_2d():
    """Input 2D list manually"""
    rows = int(input("Enter number of rows: "))
    matrix = []
    for i in range(rows):
        # Dare row user pase thi levay che
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return matrix
    # Aa nested list (2D list) return kare che

def sample_data():
    """Return sample data"""
    return [10, 20, 30, 40, 50]
    # Aa ready-made data testing mate use thay che

# ------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------
def basic_stats(data):
    """Show basic statistics"""
    print("Length:", len(data))
    # Ketla elements che

    print("Sum:", sum(data))
    # Total sum

    print("Min:", min(data))
    # Sauthi nanu value

    print("Max:", max(data))
    # Sauthi motu value

# ------------------------------
# USER DEFINED FUNCTIONS
# ------------------------------
def average(data):
    """Calculate average"""
    return sum(data) / len(data)
    # Formula: total / count

def find_duplicates(data):
    """Find duplicates"""
    return list(set([x for x in data if data.count(x) > 1]))
    # Je values ek karta vadhu vakhat ave

def unique_values(data):
    """Return unique values"""
    return list(set(data))
    # Repeat vagar na values

# ------------------------------
# *args and **kwargs
# ------------------------------
def show_args(*args):
    """Display multiple values using *args"""
    print("Values:", args)
    # args ma badha values tuple ma store thay che

def show_kwargs(**kwargs):
    """Display key-value summary"""
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        # key-value pair display kare che

# ------------------------------
# RECURSION
# ------------------------------
def factorial(n):
    """Recursive factorial"""
    if n == 1:
        return 1
    return n * factorial(n - 1)
    # Function pote j call kare che (recursion)

def fibonacci(n):
    """Recursive fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    # Fibonacci series generate kare che

# ------------------------------
# LAMBDA FUNCTIONS
# ------------------------------
def filter_data(data):
    """Filter using lambda"""
    threshold = int(input("Enter threshold: "))
    filtered = list(filter(lambda x: x > threshold, data))
    # Lambda function condition check kare che
    print("Filtered Data:", filtered)

def map_data(data):
    """Map using lambda"""
    squared = list(map(lambda x: x*x, data))
    # Dare element nu square kare che
    print("Squared Data:", squared)

# ------------------------------
# GLOBAL KEYWORD
# ------------------------------
def update_summary(data):
    """Update global summary"""
    global dataset_summary
    # Global keyword thi bahar nu variable access thay che

    dataset_summary = {
        "count": len(data),
        "mean": average(data)
    }

def show_summary():
    """Show global summary"""
    print("Dataset Summary:", dataset_summary)

# ------------------------------
# RETURN MULTIPLE VALUES
# ------------------------------
def multiple_stats(data):
    """Return min, max, avg"""
    return min(data), max(data), average(data)
    # Ek function mathi 3 values return thay che

# ------------------------------
# 2D DISPLAY
# ------------------------------
def display_2d(matrix):
    """Display 2D list"""
    for row in matrix:
        for val in row:
            print(val, end="\t")
        print()
    # Table format ma display thay che

# ------------------------------
# SORTING
# ------------------------------
def sort_data(data):
    """Sort 1D list"""
    choice = input("Ascending (A) or Descending (D)? ").lower()

    if choice == 'a':
        data.sort()
        # Ascending order
    else:
        data.sort(reverse=True)
        # Descending order

    print("Sorted Data:", data)

def sort_2d(matrix):
    """Sort 2D list"""
    sorted_matrix = sorted(matrix, key=lambda x: sum(x))
    # Row na sum pr sort thay che

    print("Sorted 2D (by row sum):")
    display_2d(sorted_matrix)

# ------------------------------
# MENU
# ------------------------------
def menu():
    data = []
    matrix = []

    while True:
        print("\n===== DATA ANALYZER =====")
        print("1. Input 1D Data")
        print("2. Input 2D Data")
        print("3. Use Sample Data")
        print("4. Basic Statistics")
        print("5. Average / Duplicates / Unique")
        print("6. *args and **kwargs")
        print("7. Recursion (Factorial/Fibonacci)")
        print("8. Lambda (Filter/Map)")
        print("9. Global Summary")
        print("10. Multiple Return Values")
        print("11. Display 2D")
        print("12. Sorting")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            data = input_1d()

        elif choice == '2':
            matrix = input_2d()

        elif choice == '3':
            data = sample_data()
            print("Sample Data:", data)

        elif choice == '4':
            basic_stats(data)

        elif choice == '5':
            print("Average:", average(data))
            print("Duplicates:", find_duplicates(data))
            print("Unique:", unique_values(data))

        elif choice == '6':
            show_args(*data)
            show_kwargs(count=len(data), sum=sum(data))

        elif choice == '7':
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))
            print("Fibonacci:", fibonacci(n))

        elif choice == '8':
            filter_data(data)
            map_data(data)

        elif choice == '9':
            update_summary(data)
            show_summary()

        elif choice == '10':
            mn, mx, avg = multiple_stats(data)
            print("Min:", mn, "Max:", mx, "Avg:", avg)

        elif choice == '11':
            display_2d(matrix)

        elif choice == '12':
            sort_data(data)
            if matrix:
                sort_2d(matrix)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

# Run program
menu()