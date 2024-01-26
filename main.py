import json
import urllib

main_path = "C:\\inetpub\\wwwrootTest"
name_config = "appsettings.json"
path_config = main_path + "\\" + name_config

dict_config = json.load(open(path_config, 'r'))

database = dict_config["Database"]
signingCertificateThumbprint = dict_config["SigningCertificateThumbprint"]
messagingService = dict_config["MessagingService"]
identityService = dict_config["IdentityService"]
storageService = dict_config["StorageService"]
rabbitMQ = dict_config["RabbitMQ"]
previewStorage = dict_config["PreviewStorage"]
signService = dict_config["SignService"]
previewService = dict_config["PreviewService"]
documentService = dict_config["DocumentService"]
officeService = dict_config["OfficeService"]
mongoDB = dict_config["MongoDB"]

folders_names = [
    "BlobStorageService",
    "CoreIdentityService",
    "CorePreviewService",
    "CoreSignService",
    "DocumentService",
    "EssService",
    "EssSite",
    "PreviewStorage"
]

for i in folders_names:
    service_path_config = main_path + "\\" + i + "\\" + name_config
    with open(service_path_config, 'r', encoding="utf-8-sig") as file:
        file_json = json.load(file)
    
    if i == "BlobStorageService":
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "CoreIdentityService":
        file_json["ConnectionStrings"]["Database"] = database
        file_json["ConnectionStrings"]["MessagingService"] = messagingService
        file_json["TokenIssuer"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "CorePreviewService":
        file_json["ConnectionStrings"]["IdentityService"] = identityService
        file_json["ConnectionStrings"]["StorageService"] = storageService
        file_json["ConnectionStrings"]["RabbitMQ"] = rabbitMQ
        file_json["ConnectionStrings"]["PreviewStorage"] = previewStorage
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "CoreSignService":
        file_json["ConnectionStrings"]["IdentityService"] = identityService
        file_json["ConnectionStrings"]["StorageService"] = storageService
        file_json["Authentication"]["TrustedIssuers"][0]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "DocumentService":
        file_json["ConnectionStrings"]["IdentityService"] = identityService
        file_json["ConnectionStrings"]["StorageService"] = storageService
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "EssService":
        file_json["ConnectionStrings"]["Database"] = database
        file_json["ConnectionStrings"]["RabbitMQ"] = rabbitMQ
        file_json["ConnectionStrings"]["IdentityService"] = identityService
        file_json["ConnectionStrings"]["StorageService"] = storageService
        file_json["ConnectionStrings"]["SignService"] = signService
        file_json["ConnectionStrings"]["PreviewService"] = previewService
        file_json["ConnectionStrings"]["PreviewStorage"] = previewStorage
        file_json["ConnectionStrings"]["MessagingService"] = messagingService
        file_json["ConnectionStrings"]["DocumentService"] = documentService
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "EssSite":
        file_json["ConnectionStrings"]["IdentityService"] = identityService
        file_json["ConnectionStrings"]["OfficeService"] = officeService
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint
    if i == "PreviewStorage":
        file_json["ConnectionStrings"]["MongoDB"] = mongoDB
        file_json["Authentication"]["SigningCertificateThumbprint"] = signingCertificateThumbprint


    with open(service_path_config, 'w', encoding="utf-8-sig") as file:
        json.dump(file_json, file, ensure_ascii=False, indent=4)

    print(i, ": Ok")
