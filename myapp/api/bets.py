from fastapi import APIRouter, HTTPException
from typing import List
from .models import BetCreate, BetResult

router = APIRouter()

# Заглушки для хранения ставок и их статусов
bets_db = []
bet_id_counter = 0


@router.post("/bets/", response_model=BetResult)
async def create_bet(bet: BetCreate):
    global bet_id_counter
    bet_id_counter += 1
    bets_db.append({"bet_id": bet_id_counter, "event_id": bet.event_id, "amount": bet.amount})
    return BetResult(bet_id=bet_id_counter, status="placed")


@router.get("/bets/", response_model=List[BetResult])
async def read_bets():
    if not bets_db:
        raise HTTPException(status_code=404, detail="No bets available")
    return [BetResult(bet_id=bet["bet_id"], status="placed") for bet in bets_db]
