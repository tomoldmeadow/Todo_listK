def view_task(listo: list) -> None:
    print("Tasks:")
    for i, t in enumerate(listo):
        print(f"{i+1}. {t}")
        print("-"*50)