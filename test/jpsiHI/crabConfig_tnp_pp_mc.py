from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName     = 'TNP_JpsiMM_5p02TeV_TuneCUETP8M1_HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3_ext1-v1'
config.General.workArea        = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs    = False

config.section_('JobType')
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'tnp_pp_mc.py'
config.JobType.outputFiles = ['tnpJPsi_MC_pp5TeV_AOD.root']

config.section_('Data')
config.Data.inputDataset  = '/JpsiMM_5p02TeV_TuneCUETP8M1/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3_ext1-v1/AODSIM'
config.Data.inputDBS      = 'global'
config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 1

config.Data.outLFNDirBase = '/store/user/%s/TagAndProbe2015/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.publication   = False

config.section_('Site')
config.Site.whitelist   = ["T2_US_MIT"]
config.Site.storageSite = 'T2_CH_CERN'