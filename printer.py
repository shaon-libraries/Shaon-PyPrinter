strComputer = "." 
import win32com.client 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_Printer") 
""" For checking go to printers & scanners"""

default_printer = [objItem.Name for objItem in colItems if objItem.Default == True][0]
print("Your Default Printer " + default_printer)

for objItem in colItems:
	if objItem.PrinterStatus == 4:
		print(objItem.Name+" is printing")
	elif objItem.PrinterStatus == 3:
		print(objItem.Name+" is idle")

"""		
While printing
	Printer Status:  4(Printing)
	Printer State:  16384(Processing)

	Printer Status:  4(printing)
	Printer State:  1024 (Printing)	
"""

for objItem in colItems:
	print("Name: " ,objItem.Name )
	#print("Caption: " ,objItem.Caption )
	#print("Device ID: " ,objItem.DeviceID )
	#print("Driver Name: " ,objItem.DriverName )
	print("Port Name: " ,objItem.PortName )
	if objItem.PrinterStatus == 4:
		print("Printer Status: Printing")
	elif objItem.PrinterStatus == 3:
		print("Printer Status: Idle")

	#print("Printer Status: " ,objItem.PrinterStatus )
	#print("Printer State: " ,objItem.PrinterState )
	print("System Name: " ,objItem.SystemName )
	print("Shared: " ,objItem.Shared )
	print("Queued: " ,objItem.Queued )
	#print("Default: " ,objItem.Default )
	#print("Local: " ,objItem.Local )
	#print("Work Offline: " ,objItem.WorkOffline )
	#print("Network: " ,objItem.Network )
	print("Capability Descriptions: " ,objItem.CapabilityDescriptions )
	print("Comment: " ,objItem.Comment )
	print("\n\n")

	#print("Printer Paper Names: " ,objItem.PrinterPaperNames )
	
	
	"""
	print("System Creation Class Name: " ,objItem.SystemCreationClassName )
	print("Print Processor: " ,objItem.PrintProcessor )
	print("Print Job Data Type: " ,objItem.PrintJobDataType )


	print("Do Complete First: " ,objItem.DoCompleteFirst )
	print("Languages Supported: " ,objItem.LanguagesSupported )
	
	print("Capabilities: " ,objItem.Capabilities )
	print("Paper Sizes Supported: " ,objItem.PaperSizesSupported )
	

	
	print("Attributes: " ,objItem.Attributes )
	print("Availability: " ,objItem.Availability )
	
	print("Vertical Resolution: " ,objItem.VerticalResolution )
	
	
	print("Raw-Only: " ,objItem.RawOnly )
	print("Priority: " ,objItem.Priority )
	
	
	print("Power Management Supported: " ,objItem.PowerManagementSupported )
	print("Power Management Capabilities: " ,objItem.PowerManagementCapabilities )
	

	print("Horizontal Resolution: " ,objItem.HorizontalResolution )
	
	
	

	
	print("______________________________-")
	
	
	print("Enable Device Query Print: " ,objItem.EnableDevQueryPrint )
	print("Extended Printer Status: " ,objItem.ExtendedPrinterStatus )
	print("Hidden: " ,objItem.Hidden )
	print("Direct: " ,objItem.Direct )
	print("Creation Class Name: " ,objItem.CreationClassName )
	print("Published: " ,objItem.Published )
	


	#not recognized
	print("Available Job Sheets: " ,objItem.AvailableJobSheets )
	print("Average Pages Per Minute: " ,objItem.AveragePagesPerMinute )
	print("Character Sets Supported: " ,objItem.CharSetsSupported )
	print("Configuration Manager Error Code: " ,objItem.ConfigManagerErrorCode )
	print("Configuration Manager User Configuration: " ,objItem.ConfigManagerUserConfig )
	print("Current Capabilities: " ,objItem.CurrentCapabilities )
	print("Current Character Set: " ,objItem.CurrentCharSet )
	print("Current Language: " ,objItem.CurrentLanguage )
	print("Current MIME Type: " ,objItem.CurrentMimeType )
	print("Current Natural Language: " ,objItem.CurrentNaturalLanguage )
	print("Current Paper Type: " ,objItem.CurrentPaperType )
	print("Default Capabilities: " ,objItem.DefaultCapabilities )
	print("Default Copies: " ,objItem.DefaultCopies )
	print("Default Language: " ,objItem.DefaultLanguage )
	print("Default MIME Type: " ,objItem.DefaultMimeType )
	print("Default Number Up: " ,objItem.DefaultNumberUp )
	print("Default Paper Type: " ,objItem.DefaultPaperType )
	print("Default Priority: " ,objItem.DefaultPriority )
	print("Description: " ,objItem.Description )
	print("Detected Error State: " ,objItem.DetectedErrorState )
	print("Enable BIDI: " ,objItem.EnableBIDI )
	print("Error Cleared: " ,objItem.ErrorCleared )
	print("Error Description: " ,objItem.ErrorDescription )
	print("Error Information: " ,objItem.ErrorInformation )
	print("Extended Detected Error State: " ,objItem.ExtendedDetectedErrorState )
	print("Installation Date: " ,objItem.InstallDate )
	print("Job Count Since Last Reset: " ,objItem.JobCountSinceLastReset )
	print("Keep Printed Jobs: " ,objItem.KeepPrintedJobs )
	print("Last Error Code: " ,objItem.LastErrorCode )
	print("Location: " ,objItem.Location )
	print("Marking Technology: " ,objItem.MarkingTechnology )
	print("Maximum Copies: " ,objItem.MaxCopies )
	print("Maximum Number Up: " ,objItem.MaxNumberUp )
	print("Maximum Size Supported: " ,objItem.MaxSizeSupported )
	print("MIME Types Supported: " ,objItem.MimeTypesSupported )
	print("Natural Languages Supported: " ,objItem.NaturalLanguagesSupported )
	print("Paper Types Available: " ,objItem.PaperTypesAvailable )
	print("Parameters: " ,objItem.Parameters )
	print("PNP Device ID: " ,objItem.PNPDeviceID )
	print("Separator File: " ,objItem.SeparatorFile )
	print("Server Name: " ,objItem.ServerName )
	print("Share Name: " ,objItem.ShareName )
	print("Spool Enabled: " ,objItem.SpoolEnabled )
	print("Start Time: " ,objItem.StartTime )
	print("Status: " ,objItem.Status )
	print("Status Information: " ,objItem.StatusInfo )
	print("Time Of Last Reset: " ,objItem.TimeOfLastReset )
	print("Until Time: " ,objItem.UntilTime )
	
	
	

	"""