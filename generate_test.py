from core.ai_generator import generate_test_code

acceptance = input("When I send a GET request, it should return 200")
code = generate_test_code(acceptance)

filename = "tests/test_generated.py"
with open(filename, "w") as f:
    f.write(code)

print(f"\n✅ Test case written to {filename}\n")
