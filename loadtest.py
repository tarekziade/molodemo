"""
Each "worker" pick a scenario randomly, given the weights and run it.
Then start again.
"""
import molotov


@molotov.scenario(weight=10)
async def scenario_one(session):
    async with session.get('http://localhost:8000') as resp:
        assert resp.status == 200


@molotov.scenario(weight=20)
async def scenario_two(session):
    async with session.get('http://localhost:8000/data.json') as resp:
        data = await resp.json()
        assert 'ok' in data
