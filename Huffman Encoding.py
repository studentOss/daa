# Practical 2: Huffman Encoding using Greedy Strategy

import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code="", codes=None):

    if codes is None:
        codes = {}

    if root is None:
        return codes

    # If leaf node
    if root.char is not None:
        codes[root.char] = code
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


# Huffman Encoding
def huffman_encoding(text):

    # Step 1: Calculate frequency
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    print("\nCharacter Frequencies:")
    for char, freq in frequency.items():
        print(char, ":", freq)

    # Step 2: Create min heap
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Step 3: Build Huffman Tree
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)

        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    # Root of Huffman Tree
    root = heap[0]

    # Step 4: Generate codes
    codes = generate_codes(root)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(char, ":", code)

    # Step 5: Encode the text
    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    print("\nEncoded Message:")
    print(encoded_text)


# Main program
text = input("Enter the text: ")

if text:
    huffman_encoding(text)
else:
    print("Please enter some text.")