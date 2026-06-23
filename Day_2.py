# Calculate the prime number




# To understand whether a number is prime, we have to look at its mathematical definition: a prime number is a whole number greater than 1 that has exactly two divisors: 1 and itself. If a number can be divided evenly by any other number, it is composite.Here is the step-by-step logic used to write the most efficient Python code for checking prime numbers.1. The Core Logic: Eliminating the ObviousThe very first check we do is for numbers less than or equal to 1 (like 0, 1, or negative numbers). By definition, these cannot be prime.Pythonif n <= 1:
#     return False
# 2. The Naive Approach (The "Check Everything" Method)The most intuitive way to check if a number $n$ is prime is to try dividing it by every single number from $2$ up to $n - 1$. If any of those numbers divides $n$ perfectly (meaning the remainder is 0), then it's not prime.In Python, we check the remainder using the modulo operator (%).Python# If n % i == 0, it means 'i' divides 'n' perfectly
# if n % i == 0:
#     return False
# While this works, it is very slow for large numbers. If you want to check if $1,000,003$ is prime, your loop has to run a million times!3. The Optimized Approach: The Square Root RuleWe can make this code incredibly fast using a clever math property: factors always come in pairs.Let's look at the factors of the composite number 36:$2 \times 18 = 36$$3 \times 12 = 36$$4 \times 9 = 36$$6 \times 6 = 36$ (The square root: $\sqrt{36} = 6$)$9 \times 4 = 36$$12 \times 3 = 36$$18 \times 2 = 36$Notice that after $6 \times 6$, the factor pairs just repeat themselves in reverse order ($4 \times 9$ becomes $9 \times 4$).Therefore, if a number has a factor, at least one of those factors must be less than or equal to its square root ($\sqrt{n}$). If we don't find a factor by the time we reach $\sqrt{n}$, the number is guaranteed to be prime.Translating Math to Python CodeTo implement the square root rule in Python:Find the square root: We use n0.5.Convert it to an integer: Python's range() function only accepts integers, so we use int(n0.5).Include the boundary: The range(start, stop) function in Python stops just before the stop value. To make sure we actually check the square root itself, we must add 1: int(n0.5) + 1.The Complete CodePutting it all together, here is the clean, optimized function:Pythondef is_prime(n):
#     # Step 1: Numbers less than or equal to 1 are not prime
#     if n <= 1:
#         return False
    
#     # Step 2: Check factors from 2 up to the square root of n
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False  # Found a factor! Not prime.
            
#     # Step 3: If the loop finishes without finding a factor, it's prime
#     return True

# # --- Testing the code ---
# numbers_to_test = [1, 2, 4, 11, 25, 29]

# for num in numbers_to_test:
#     print(f"Is {num} prime? {is_prime(num)}")
# Why this logic matters:If you pass the number 100,000,000,000,000,007 into the naive approach, your computer will freeze trying to run 100 quadrillion loops.With the square root logic, $\sqrt{100,000,000,000,000,007}$ is roughly 10,000,000. The computer only has to run 10 million loops, which Python executes in a fraction of a second!
# x = 10 
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True










# Sieve of eratosthenes







# Ugly Numbers : An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.






x = 10 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1. Call the function and print the result
result = is_prime(x)
print(f"Is {x} a prime number? {result}")

# 2. Or test it with another number directly
print(f"Is 7 a prime number? {is_prime(7)}")

# for i in range (100):
#     if is_prime(i)
