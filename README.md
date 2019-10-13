# Django-graphql
Trying graphql with Django


Trying out with http://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/

It Actually does work,
The below query gives,

```graphql
query{
  allIngredients{
    id
    name
    notes
  }
}
```
Output 👇
```json
{
  "data": {
    "allIngredients": [
      {
        "id": "1",
        "name": "Eggs",
        "notes": "Good old eggs"
      },
      {
        "id": "2",
        "name": "Milk",
        "notes": "Comes from a cow"
      },
      {
        "id": "3",
        "name": "Beef",
        "notes": "Much like milk, this comes from a cow"
      },
      {
        "id": "4",
        "name": "Chicken",
        "notes": "Definitely doesn't come from a cow"
      }
    ]
  }
}
```
