import com.sap.gateway.ip.core.customdev.util.Message;
import com.sap.it.api.ITApiFactory;
import com.sap.it.api.securestore.SecureStoreService
import com.sap.it.api.securestore.exception.SecureStoreException

def Message processData(Message message) {
    def apiKeyAlias = message.getProperty("eu-bp-dependants-api-key-alias")
    def secureStorageService =  ITApiFactory.getService(SecureStoreService.class, null)
    try{
        def secureParameter = secureStorageService.getUserCredential(apiKeyAlias)
        def apiKey = secureParameter.getPassword().toString()
        message.setHeader("apiKey", apiKey)
    } catch(Exception e){
        throw new SecureStoreException("Secure Parameter not available")
    }
    return message;
}