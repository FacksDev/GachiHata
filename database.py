async def collect_tasks():
    pass


async def create_users(db, model):
    all_users = await db.all(model.query)

    if not len(all_users):
        await model.create(
            user_id=858295159,
            name="Andrey"
        )

        await model.create(
            user_id=399828804,
            name="BloodRedTape"
        )

        await model.create(
            user_id=498016821,
            name="Jeytery"
        )


async def create_tasks(db, model):
    all_tasks = await db.all(model.query)

    default_tasks = [
        ("Кухня плита/столы", 5, 14),
        ("Кухня пол", 3, 14),
    ]

    if len(all_tasks) < len(default_tasks):
        await model.delete.where(True).gino.status()

        for name, value, repeat_days in default_tasks:
            await model.create(
                name=name,
                value=value,
                repeat_days=repeat_days
            )


async def assign_task(task, user):
    pass


async def get_rating() -> dict:
    pass
