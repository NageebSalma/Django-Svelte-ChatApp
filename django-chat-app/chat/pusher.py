import pusher
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
pusher_client = pusher.Pusher(
  app_id=env('APP_ID'),
  key=env('KEY'),
  secret=env('SECRET'),
  cluster='eu',
  ssl=True
)

