import uos, gc, sys, system, virtualtimers

folders = ['lib', 'apps', 'cache', 'cache/woezel', 'config']
for folder in folders:
    try:
        uos.mkdir(folder)
    except Exception as error:
        pass

del folders, uos
gc.collect()

## Make badge sleep in undervoltage conditions
virtualtimers.activate(1000) # low resolution needed
def _vcc_callback():
    try:
        vcc = system.get_vcc_bat()
        if vcc != None:
            if vcc < 3300:
                __import__('deepsleep')
                deepsleep.vcc_low()
    finally:
        # Return 10000 to start again in 10 seconds
        gc.collect()
        return 10000

virtualtimers.new(10000, _vcc_callback, hfpm=True)
