from agent import generate_guided_tour


def main():
    print("=== GitHub Guided Tour Agent ===\n")
    repo_name = input("Enter GitHub repository (owner/repo): ")

    try:
        result = generate_guided_tour(repo_name)
        print("\n===== AI GENERATED GUIDED TOUR =====\n")
        print(result)

    except Exception as e:
        print("\n An error occurred:")
        print(e)


if __name__ == "__main__":
    main()
