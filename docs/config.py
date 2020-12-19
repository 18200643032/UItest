import os
import time
config_yaml_path = os.path.join(os.path.dirname(__file__),'config.yaml').replace("\\","/")
login_yaml_path = os.path.join(os.path.dirname(__file__),'login.yaml').replace("\\","/")
log_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),'report'),'Logs').replace("\\","/")
now = time.strftime('%Y-%m-%d_%H_%M_%S')
reportname = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),'report'),'TestResult/').replace("\\","/"),'TestResult' + now + '.html').replace("\\","/")
