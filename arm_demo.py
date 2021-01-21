from arm_controller import ArmController

ac=ArmController()
ac.set_joints([.2,-.5,.3,-.4])
ac.set_joints([-.3,-.6,.7,.9])
ac.set_joints([0,0,0,0])
print(ac.get_pose())
