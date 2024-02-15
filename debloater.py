import os

package_names = [
    "com.mobvoi.wear.bloodoxygen",
    "com.mobvoi.wear.calculator.aw",
    "com.mobvoi.wear.privacy.aw",
    "com.mobvoi.ticwatch.jupiter.home",
    "com.google.android.wearable.overlay.home.mobvoi.tiles",
    "com.mobvoi.wear.fitness.aw",
    "com.mobvoi.wear.breath",
    "com.mobvoi.wear.account.aw",
    "com.mobvoi.whs.gps",
    "com.mobvoi.wear.sleep.aw",
    "com.mobvoi.wear.pressure",
    "com.mobvoi.wear.appsservice",
    "com.mobvoi.wear.heartrate.aw",
    "com.mobvoi.wear.health.aw",
    "com.mobvoi.mwf.magicfaces",
    "android.autoinstalls.config.mobvoi.rover",
    "com.mobvoi.care",
    "com.mobvoi.wear.refsysui",
    "com.mobvoi.companion.aw",
    "com.mobvoi.wear.watchface.aw",
    "com.mobvoi.wear.watchface.p5",
    "com.mobvoi.wear.system.aw"
]
hostname = input("enter ticwatch hostname, omit the port number. ") + ":5555"
os.system("adb connect " + hostname)
for package in package_names:
    os.system("adb shell pm disable-user --user 0 " + package)