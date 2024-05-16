from typing import List
from fastapi import HTTPException, APIRouter

from myapp.api.models import BetCreate, BetResult


router = APIRouter()

# Заглушки для хранения ставок и их статусов
bets_db = []
bet_id_counter = 0


@router.post("/")
async def create_bet(bet: BetCreate) -> BetResult:
    global bet_id_counter
    bet_id_counter += 1
    bets_db.append({"bet_id": bet_id_counter, "event_id": bet.event_id, "amount": bet.amount})
    return BetResult(bet_id=bet_id_counter, status="placed")


@router.get("/")
async def read_bets() -> List[BetResult]:
    if not bets_db:
        raise HTTPException(status_code=404, detail="No bets available")
    return [BetResult(bet_id=bet["bet_id"], status="placed") for bet in bets_db]
