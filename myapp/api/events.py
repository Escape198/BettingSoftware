from fastapi import APIRouter

router = APIRouter()


events_db = []


@router.put("/events/{event_id}")
async def update_event(event_id: int, status: str):
    for event in events_db:
        if event["event_id"] == event_id:
            event["status"] = status
    return {"message": f"Event {event_id} status updated to {status}"}
