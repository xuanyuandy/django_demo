from envx.models import Env

def fake_env_data():
    Env.objects.all().delete()
    print('delete all env data')
    # 给相对应的对象创建数据
    Env.objects.create(name="DEV", eid=1)
    Env.objects.create(name="TEST", eid=2)
    Env.objects.create(name="PRD", eid=3)
    print('create all env data')