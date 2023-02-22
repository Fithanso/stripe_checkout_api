Swagger is available at {domain}/swagger/schema/

Admin credentials: admin/admin

DB comes ready, you don't need to apply migrations

To launch your project:
1) clone it
2) install everything from requirements.txt
3) run manage.py runserver

For endpoints {domain}/buy and {domain}/item you must provide "item_ids" GET parameter.<br>
Example: {domain}/buy?item_ids=1,2,3