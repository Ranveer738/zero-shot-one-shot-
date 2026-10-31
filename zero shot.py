from grog import generate_response
# switch to:
# from hf import generate_response

def run():
    category = input("Enter a category (e.g., animal, food, city): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()


    # Zero-shot example
    zero_shot = f"Is {item} a {category}? Answer yes or no."
    print("\n--- ZERO-SHOT LEARNING ---")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")


    one_shot = f"""Example:
    Category: fruit
    Item: apple
    Answer: Yes, apple is a fruit.

        Now you try:
        Category: {category}
        Item: {item}
        Answer:"""
    print("\n--- ONE-SHOT LEARNING ---")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")


    few_shot = f"""Example 1:
    Category: fruit
    Item: apple
    Answer: Yes, apple is a fruit.

    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("\n--- FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(few_shot, temperature=0.5, max_tokens=1024)}")


    # Creative task
    creative_prompt = f"""Write a one-sentence story about the given word.

Example 1: Word: moon
Story: The moon lit up the night sky as a little astronaut began an exciting space adventure.

Word: {item}
Story:"""
    print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.9, max_tokens=1024)}")

if __name__ == "__main__":
 run()

