from pydantic import BaseModel, validator


class BetCreate(BaseModel):
    event_id: str
    amount: float

    @classmethod
    @validator("amount")
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("amount must be a positive number")
        return v


class BetResult(BaseModel):
    bet_id: int
    status: str
