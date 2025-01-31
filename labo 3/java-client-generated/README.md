# swagger-java-client

API de Gestion des Cours en Ligne - OpenAPI 3.0
- API version: 1.0.0
  - Build date: 2024-11-11T15:14:48.525836921Z[GMT]

Ceci est une API permettant de gérer le contenu des cours en ligne. Elle expose des fonctionnalités pour créer, consulter, mettre à jour, et supprimer des cours et leurs séances. 


*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CoursApi;

import java.io.File;
import java.util.*;

public class CoursApiExample {

    public static void main(String[] args) {
        
        CoursApi apiInstance = new CoursApi();
        try {
            List<Cours> result = apiInstance.coursGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CoursApi#coursGet");
            e.printStackTrace();
        }
    }
}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CoursApi;

import java.io.File;
import java.util.*;

public class CoursApiExample {

    public static void main(String[] args) {
        
        CoursApi apiInstance = new CoursApi();
        String id = "id_example"; // String | 
        try {
            apiInstance.coursIdDelete(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CoursApi#coursIdDelete");
            e.printStackTrace();
        }
    }
}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CoursApi;

import java.io.File;
import java.util.*;

public class CoursApiExample {

    public static void main(String[] args) {
        
        CoursApi apiInstance = new CoursApi();
        String id = "id_example"; // String | 
        try {
            Cours result = apiInstance.coursIdGet(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CoursApi#coursIdGet");
            e.printStackTrace();
        }
    }
}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CoursApi;

import java.io.File;
import java.util.*;

public class CoursApiExample {

    public static void main(String[] args) {
        
        CoursApi apiInstance = new CoursApi();
        Cours body = new Cours(); // Cours | 
        String id = "id_example"; // String | 
        try {
            apiInstance.coursIdPut(body, id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CoursApi#coursIdPut");
            e.printStackTrace();
        }
    }
}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CoursApi;

import java.io.File;
import java.util.*;

public class CoursApiExample {

    public static void main(String[] args) {
        
        CoursApi apiInstance = new CoursApi();
        Cours body = new Cours(); // Cours | 
        try {
            apiInstance.coursPost(body);
        } catch (ApiException e) {
            System.err.println("Exception when calling CoursApi#coursPost");
            e.printStackTrace();
        }
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoursApi* | [**coursGet**](docs/CoursApi.md#coursGet) | **GET** /cours | Obtenir la liste des cours
*CoursApi* | [**coursIdDelete**](docs/CoursApi.md#coursIdDelete) | **DELETE** /cours/{id} | Supprimer un cours
*CoursApi* | [**coursIdGet**](docs/CoursApi.md#coursIdGet) | **GET** /cours/{id} | Obtenir un cours par son identifiant
*CoursApi* | [**coursIdPut**](docs/CoursApi.md#coursIdPut) | **PUT** /cours/{id} | Mettre à jour un cours existant
*CoursApi* | [**coursPost**](docs/CoursApi.md#coursPost) | **POST** /cours | Ajouter un nouveau cours
*SeancesApi* | [**coursIdSeancesGet**](docs/SeancesApi.md#coursIdSeancesGet) | **GET** /cours/{id}/seances | Obtenir la liste des séances d&#x27;un cours

## Documentation for Models

 - [Cours](docs/Cours.md)
 - [Seance](docs/Seance.md)

## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

support@exemple.com
