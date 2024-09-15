from fastapi import FastAPI, HTTPException

app = FastAPI()

# Mock data representing Colombian teams
teams = {
    1: {"id": 1, "name": "Atlético Nacional", "city": "Medellín"},
    2: {"id": 2, "name": "Millonarios", "city": "Bogotá"},
    3: {"id": 3, "name": "América de Cali", "city": "Cali"},
}

@app.get("/teams/{team_id}")
async def get_team(team_id: int):
    team = teams.get(team_id)
    content = {}
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    content['data'] = team
    return content 
