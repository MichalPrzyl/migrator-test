import os


def create_migration_for_application(
        app: str, 
        migration_number: int,
        migration_file_name: str,
        dependencies: list[str]):
    dependencies_str = ", ".join([f'("{dep[0]}", "{dep[1]}")' for dep in dependencies])
    print(f"dependencies_str: {dependencies_str}")
            # """from django.db import migrations, models


    migration_content = f"""class Migration(migrations.Migration):
        dependencies = [{dependencies_str}]

        operations = [
            migrations.DeleteModel("Tribble"),
            migrations.AddField("Author", "rating", models.IntegerField(default=0)),
    ]"""

    with open(f"{app}/migrations/{migration_number}_{migration_file_name}.py", "w") as file:
        file.write(migration_content)


os.makedirs('main_app/migrations')
create_migration_for_application("main_app", '0001', 'start', [])
create_migration_for_application("main_app", '0002', 'another_one', [('main_app', '0001_start')])
create_migration_for_application("main_app", '0003', 'another_one_third', [('main_app', '0002_another_one_jeb_sie')])
