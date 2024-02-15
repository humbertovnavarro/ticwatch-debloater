import os

package_names = [
    "com.mobvoi.companion.aw",
    "com.mobvoi.ticwatch.jupiter.home",
    "com.mobvoi.wear.account.aw",
    "com.mobvoi.wear.appsservice",
    "com.mobvoi.wear.bloodoxygen",
    "com.mobvoi.wear.breath",
    "com.mobvoi.wear.calculator.aw",
    "com.mobvoi.wear.fitness.aw",
    "com.mobvoi.wear.health.aw",
    "com.mobvoi.wear.heartrate.aw",
    "com.mobvoi.wear.overlay.mcuservice",
    "com.mobvoi.wear.pressure",
    "com.mobvoi.wear.privacy.aw",
    "com.mobvoi.wear.sleep.aw",
    "com.mobvoi.wear.system.aw",
    "com.mobvoi.wear.watchface.aw",
    "com.mobvoi.mwf.magicfaces",
    "com.mobvoi.care",
    "com.mobvoi.wear.watchface.p5"
]

hostname = input("enter ticwatch hostname and port (i.e. 192.168.1.100:5555)\n")
os.system("adb connect " + hostname)
for package in package_names:
    os.system("adb shell pm disable-user --user 0 " + package)