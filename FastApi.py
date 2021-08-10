from fastapi import FastAPI, Path

tits = FastAPI()

inventory = {
    1: {
        'name': 'milk',
        'price': 3.99,
        'brand': 'dairy milk'
    }
}


@tits.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None,
                                 description='put id in or else...')):
    return inventory[item_id]


@tits.get('/get-by-name/{item_id}')
def get_item(*, item_id: int, name: str = None, test: int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data': 'Not Found'}
