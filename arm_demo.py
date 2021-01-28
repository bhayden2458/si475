from arm_controller import ArmController

ac=ArmController()
ac.set_joints([0,0,0,0])
ac.set_joints([.5,.5,.25,0])
print(ac.get_pose())
