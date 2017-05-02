*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Telnet.
Library           Telnet

*** Variables ***
${fail}	Error:

*** Keywords ***
Open Telnet To Login Page
	open_connection	10.1.25.133
	Login	manage	!manage
	
Set pager off
	Write	set cli-parameters pager off
	read_until	expected=#
	

Print disks
	Write	show disks
	read_until	expected=#
	
	
Read until prompt
	read_until	expected=#
	
Read output
	read
	
Read until message
	read_until expected=Connection to host lost.
	
Print system
	Write	show system
	read_until	expected=#

	
Print versions
	Write	show versions
	read_until	expected=#

	
Print version details
	Write	show version detail
	read_until	expected=#

	
Print snap pools
	Write	show snap-pools
	read_until	expected=#
	
	
Print volumes
	Write	show volumes
	read_until	expected=#
	

Print snapshots
	Write	show snapshots
	read_until	expected=#
	
	
Print host-parameters
	Write	show host-parameters
	read_until	expected=#
	
	
Print iniatiators
	Write	show initiators
	read_until	expected=#
	

Print volume-maps
	Write	show volume-maps
	read_until	expected=#
	
	
Print enclosure
	Write	show enclosures
	read_until	expected=#
	
	
Print disk-enclosures
	Write	show disks encl
	read_until	expected=#
	

Print fde-state
	Write	show fde-state
	read_until	expected=#
	
	
Print license
	Write	show license
	read_until	expected=#
	
	
Print protocols
	Write	show protocols
	read_until	expected=#
	
	
Print advanced-settings
	Write	show advanced-settings
	read_until	expected=#
	
	
Print ntp-status
	Write	show ntp-status
	read_until	expected=#
	
	
Print users
	Write	show users
	read_until	expected=#
	
	
Print schedules
	Write	show schedules
	read_until	expected=#
	
	
Print tasks
	Write	show tasks
	read_until	expected=#
	
Write exit
	Write	exit
	