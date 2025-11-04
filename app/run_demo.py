from app.main import create_llm, generate_from_example
from app.examples import ALL_EXAMPLES


def run_demo():
    print("=== LangChain Content Agent Demo ===\n")

    llm = create_llm()

    for i, example in enumerate(ALL_EXAMPLES, 1):
        print(f"[{i}/{len(ALL_EXAMPLES)}] Processing: {example['name']}")

        try:
            result = generate_from_example(example, llm)

            text_preview = (
                result.text[:80] + "..." if len(result.text) > 80 else result.text
            )
            print(f"  Text: {text_preview}")

            if hasattr(result, "hooks"):
                print(f"  Hooks: {len(result.hooks)}")
            if hasattr(result, "ctas"):
                print(f"  CTAs: {len(result.ctas)}")
            if hasattr(result, "hashtags"):
                print(f"  Hashtags: {len(result.hashtags)}")

            print()

        except Exception as e:
            print(f"  Error: {e}\n")


if __name__ == "__main__":
    run_demo()
