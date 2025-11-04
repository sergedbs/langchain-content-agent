from app.main import create_llm, generate_content
from app.models.outputs import EventContentOutput, ProjectContentOutput
from app.examples import ALL_EXAMPLES


def run_demo():
    print("=== LangChain Content Agent Demo ===\n")

    llm = create_llm()

    for i, example in enumerate(ALL_EXAMPLES, 1):
        print("=" * 80)
        print(f"[{i}/{len(ALL_EXAMPLES)}] {example['name']}")
        print("=" * 80)

        try:
            result = generate_content(example, llm)

            print(f"\nTITLE:\n{result.title}\n")

            print(f"TEXT:\n{result.text}\n")

            print("HOOKS:")
            for idx, hook in enumerate(result.hooks, 1):
                print(f"  {idx}. {hook}")

            print("\nCTAs:")
            for idx, cta in enumerate(result.ctas, 1):
                print(f"  {idx}. {cta}")

            print("\nHASHTAGS:")
            print(f"  {' '.join(result.hashtags)}")

            if isinstance(result, EventContentOutput):
                if result.stories_variant:
                    print(f"\nSTORIES VARIANT:\n{result.stories_variant}")

                if result.reel_variant:
                    print(f"\nREEL VARIANT:\n{result.reel_variant}")

                if result.carousel_variant:
                    print("\nCAROUSEL VARIANT:")
                    for idx, slide in enumerate(result.carousel_variant, 1):
                        print(f"  Slide {idx}: {slide}")

            if isinstance(result, ProjectContentOutput):
                if result.variant_a:
                    print(f"\nVARIANT A:\n{result.variant_a}")

                if result.variant_b:
                    print(f"\nVARIANT B:\n{result.variant_b}")

                if result.platform_specific_notes:
                    print(f"\nPLATFORM NOTES:\n{result.platform_specific_notes}")

            print("\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    run_demo()
