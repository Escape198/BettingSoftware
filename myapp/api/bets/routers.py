from typing import List
from fastapi import APIRouter

from .handlers import create_bet, read_bets
from myapp.api.models import BetResult


router = APIRouter()

router.post("/bets/", response_model=BetResult)(create_bet)
router.get("/bets/", response_model=List[BetResult])(read_bets)
