
def base_funziona(drive):
    print("configuring...")
    drive.axis1.controller.config.pos_gain = 3
    drive.config.brake_resistance = 3
    drive.axis1.motor.config.pole_pairs = 7 
    drive.axis1.encoder.config.cpr = 8192
    drive.axis1.controller.config.vel_gain = 0.4 #0.2
    drive.axis1.controller.config.vel_integrator_gain = 0.25
    drive.axis1.controller.config.pos_gain = 1.5
    drive.axis1.controller.config.vel_limit = 5
    drive.axis1.controller.config.enable_overspeed_error = False
    print("done")
    drive.save_configuration()
    print("saved")

def initial_conf1(drive):
    print("configuring...")
    drive.axis1.controller.config.pos_gain = 3
    drive.config.brake_resistance = 3
    drive.axis1.motor.config.pole_pairs = 7 
    drive.axis1.encoder.config.cpr = 8192
    drive.axis1.controller.config.vel_gain = 0.4 #0.2
    drive.axis1.controller.config.vel_integrator_gain = 0.25
    drive.axis1.controller.config.pos_gain = 1.5
    drive.axis1.controller.config.vel_limit = 5
    drive.axis1.controller.config.enable_overspeed_error = False
    print("done")
    drive.save_configuration()
    print("saved")


CONFIGS = [base_funziona, initial_conf1]
CONF_INDEX_SELECTOR = 0

def call_config(drive):
    CONFIGS[CONF_INDEX_SELECTOR](drive)