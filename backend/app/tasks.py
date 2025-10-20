
from .celery_worker import celery_app
from .models.base import SessionLocal, Subscription
import datetime

@celery_app.task
def check_expired_subscriptions():
    """
    A periodic Celery task to check for and deactivate expired subscriptions.
    """
    print("Running scheduled task: Checking for expired subscriptions...")

    db = SessionLocal()
    try:
        now = datetime.datetime.utcnow()

        # Find all active subscriptions that have expired
        expired_subscriptions = db.query(Subscription).filter(
            Subscription.is_active == True,
            Subscription.end_date <= now
        ).all()

        if not expired_subscriptions:
            print("No expired subscriptions found.")
            return {"message": "No expired subscriptions found."}

        for sub in expired_subscriptions:
            print(f"Deactivating subscription for user_id: {sub.user_id}")
            sub.is_active = False

        db.commit()

        print(f"Successfully deactivated {len(expired_subscriptions)} subscriptions.")
        return {"message": f"Deactivated {len(expired_subscriptions)} subscriptions."}

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
        # In a real app, you would have more robust error handling/logging
        return {"error": str(e)}
    finally:
        db.close()
