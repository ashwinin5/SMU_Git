*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resources.robot

*** Test Cases ***
Valid Login
    Open Telnet To Login Page
	Set pager off
	Print disks
	Print system
	Print versions
	Print version details
	Print snap pools
	Print volumes
	Print snapshots
	Print host-parameters
	Print iniatiators
	Print volume-maps
	Print enclosure
	Print disk-enclosures
	Print fde-state
	Print license
	Print protocols
	Print advanced-settings
	Print ntp-status
	Print users
	Print schedules
	Print tasks
	Write exit
	[Teardown]    Close All Connections