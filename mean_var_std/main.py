from test_module import TestCalculate
import mean_var_std
import unittest

# Test with example input
test_list = [0,1,2,3,4,5,6,7,8]
print("Testing with list:", test_list)
try:
    result = mean_var_std.calculate(test_list)
    print("\nResults:")
    for key, value in result.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error: {e}")

# Run unit tests
if __name__ == "__main__":
    unittest.main(argv=['ignored', '-v'])