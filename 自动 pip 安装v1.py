try:
    import time
except ImportError as e:
    module_name = str(e).split("'")[1]
    print(f"需要安装{module_name}库")
    # 在当前Python版本中运行pip安装numpy库
    import subprocess
    import sys

    def run_pip(*args):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", *args])
        except subprocess.CalledProcessError as e:
            print(f"运行pip时出错：{e}")
    run_pip("install", module_name)
