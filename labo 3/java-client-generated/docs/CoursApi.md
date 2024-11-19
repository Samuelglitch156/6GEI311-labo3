# CoursApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coursGet**](CoursApi.md#coursGet) | **GET** /cours | Obtenir la liste des cours
[**coursIdDelete**](CoursApi.md#coursIdDelete) | **DELETE** /cours/{id} | Supprimer un cours
[**coursIdGet**](CoursApi.md#coursIdGet) | **GET** /cours/{id} | Obtenir un cours par son identifiant
[**coursIdPut**](CoursApi.md#coursIdPut) | **PUT** /cours/{id} | Mettre à jour un cours existant
[**coursPost**](CoursApi.md#coursPost) | **POST** /cours | Ajouter un nouveau cours

<a name="coursGet"></a>
# **coursGet**
> List&lt;Cours&gt; coursGet()

Obtenir la liste des cours

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CoursApi;


CoursApi apiInstance = new CoursApi();
try {
    List<Cours> result = apiInstance.coursGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CoursApi#coursGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Cours&gt;**](Cours.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="coursIdDelete"></a>
# **coursIdDelete**
> coursIdDelete(id)

Supprimer un cours

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CoursApi;


CoursApi apiInstance = new CoursApi();
String id = "id_example"; // String | 
try {
    apiInstance.coursIdDelete(id);
} catch (ApiException e) {
    System.err.println("Exception when calling CoursApi#coursIdDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="coursIdGet"></a>
# **coursIdGet**
> Cours coursIdGet(id)

Obtenir un cours par son identifiant

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CoursApi;


CoursApi apiInstance = new CoursApi();
String id = "id_example"; // String | 
try {
    Cours result = apiInstance.coursIdGet(id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CoursApi#coursIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  |

### Return type

[**Cours**](Cours.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="coursIdPut"></a>
# **coursIdPut**
> coursIdPut(body, id)

Mettre à jour un cours existant

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CoursApi;


CoursApi apiInstance = new CoursApi();
Cours body = new Cours(); // Cours | 
String id = "id_example"; // String | 
try {
    apiInstance.coursIdPut(body, id);
} catch (ApiException e) {
    System.err.println("Exception when calling CoursApi#coursIdPut");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cours**](Cours.md)|  |
 **id** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="coursPost"></a>
# **coursPost**
> coursPost(body)

Ajouter un nouveau cours

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CoursApi;


CoursApi apiInstance = new CoursApi();
Cours body = new Cours(); // Cours | 
try {
    apiInstance.coursPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling CoursApi#coursPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cours**](Cours.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

