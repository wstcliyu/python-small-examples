### 66 ʹ��װ����

from functools import wraps
import time

def print_info(f):
    """
    @para: f, ��κ�������
    """
    @wraps(f) # ȷ������f���Ƶ����Բ������ı�
    def info():
        print('���ڵ��ú�������Ϊ�� %s ' % (f.__name__,))
        t1 = time.time()
        f()
        t2 = time.time()
        delta = (t2 - t1)
        print('%s ����ִ��ʱ��Ϊ��%f s' % (f.__name__,delta))

    return info
        

@print_info
def f1():
    time.sleep(1.0)


@print_info
def f2():
    time.sleep(2.0)


f1()
f2()

# �����Ϣ���£�

# ���ڵ��ú�������Ϊ�� f1
# f1 ����ִ��ʱ��Ϊ��1.000000 s
# ���ڵ��ú�������Ϊ�� f2
# f2 ����ִ��ʱ��Ϊ��2.000000 s