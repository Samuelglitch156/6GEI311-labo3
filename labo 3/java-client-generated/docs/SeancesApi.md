# SeancesApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coursIdSeancesGet**](SeancesApi.md#coursIdSeancesGet) | **GET** /cours/{id}/seances | Obtenir la liste des séances d&#x27;un cours

<a name="coursIdSeancesGet"></a>
# **coursIdSeancesGet**
> List&lt;Seance&gt; coursIdSeancesGet(id)

Obtenir la liste des séances d&#x27;un cours

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.SeancesApi;


SeancesApi apiInstance = new SeancesApi();
String id = "id_example"; // String | 
try {
    List<Seance> result = apiInstance.coursIdSeancesGet(id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SeancesApi#coursIdSeancesGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  |

### Return type

[**List&lt;Seance&gt;**](Seance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

