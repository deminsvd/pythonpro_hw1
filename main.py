if __name__ == '__main__':
    from application.salary import salary
    from application.db.people import people
    from datetime import date
    import aiodi

    salary()
    people()
    print(date.today())