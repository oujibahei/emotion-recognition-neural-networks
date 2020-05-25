from celery import Celery
import celeryconfig 

app = Celery('tasks')
app.config_from_object(celeryconfig)
app.conf.humanize(with_defaults=False, censored=True)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(1.0, clustering.s(), name='clustering every 10')
    sender.add_periodic_task(1.0, messaging.s(), name='messaging every 10')

@app.task
def get_face(file):
    print('return face!')
    pass

@app.task
def clustering():
    print('clustered!')
    pass

@app.task
def messaging():
    print('message out!')
    pass
