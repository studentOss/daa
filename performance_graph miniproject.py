
import time
import random


# ==========================================
# 1. NAIVE STRING MATCHING ALGORITHM
# ==========================================

def naive_string_matching(text, pattern):

    n = len(text)
    m = len(pattern)

    positions = []
    comparisons = 0

    # Check every possible position
    for i in range(n - m + 1):

        j = 0

        # Compare pattern characters with text
        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        # If all characters match
        if j == m:
            positions.append(i)

    return positions, comparisons


# ==========================================
# 2. RABIN-KARP STRING MATCHING ALGORITHM
# ==========================================

def rabin_karp(text, pattern):

    n = len(text)
    m = len(pattern)

    positions = []
    comparisons = 0

    if m == 0:
        return list(range(n + 1)), comparisons

    if m > n:
        return positions, comparisons

    d = 256
    q = 101

    pattern_hash = 0
    text_hash = 0
    h = 1

    # Calculate h = d^(m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate initial hash values
    for i in range(m):

        pattern_hash = (
            d * pattern_hash + ord(pattern[i])
        ) % q

        text_hash = (
            d * text_hash + ord(text[i])
        ) % q

    # Slide pattern over text
    for i in range(n - m + 1):

        # Check hash values
        if pattern_hash == text_hash:

            # Verify actual characters
            j = 0

            while j < m:
                comparisons += 1

                if text[i + j] != pattern[j]:
                    break

                j += 1

            if j == m:
                positions.append(i)

        # Calculate hash for next window
        if i < n - m:

            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            text_hash = (text_hash + q) % q

    return positions, comparisons


# ==========================================
# 3. PERFORMANCE COMPARISON
# ==========================================

def compare_performance(text, pattern):

    print("\n========== PERFORMANCE COMPARISON ==========")

    # Naive Algorithm
    start = time.perf_counter()

    naive_result, naive_comparisons = (
        naive_string_matching(text, pattern)
    )

    naive_time = time.perf_counter() - start

    # Rabin-Karp Algorithm
    start = time.perf_counter()

    rk_result, rk_comparisons = (
        rabin_karp(text, pattern)
    )

    rk_time = time.perf_counter() - start

    print("\nNAIVE STRING MATCHING")
    print("Occurrences:", naive_result)
    print("Number of comparisons:", naive_comparisons)
    print("Execution time:", naive_time, "seconds")

    print("\nRABIN-KARP ALGORITHM")
    print("Occurrences:", rk_result)
    print("Number of comparisons:", rk_comparisons)
    print("Execution time:", rk_time, "seconds")

    print("\n========== FINAL RESULT ==========")

    if naive_result == rk_result:
        print("Both algorithms produced the same result.")
    else:
        print("Results do not match!")

    if naive_time < rk_time:
        print("Naive algorithm was faster for this input.")
    elif rk_time < naive_time:
        print("Rabin-Karp algorithm was faster for this input.")
    else:
        print("Both algorithms took approximately equal time.")


# ==========================================
# 4. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("======================================")
    print(" DAA MINI PROJECT")
    print(" STRING MATCHING ALGORITHMS")
    print("======================================")

    text = input("\nEnter the text: ")
    pattern = input("Enter the pattern: ")

    if not pattern:
        print("Pattern cannot be empty.")
    else:
        compare_performance(text, pattern)
