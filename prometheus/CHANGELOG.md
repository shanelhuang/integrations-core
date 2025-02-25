# CHANGELOG - Prometheus

## 3.4.0 / 2022-02-19 / Agent 7.35.0

***Added***: 

* Add `pyproject.toml` file. See [#11421](https://github.com/DataDog/integrations-core/pull/11421).

***Fixed***: 

* Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).


## 3.3.1 / 2021-03-07 / Agent 7.27.0

***Fixed***: 

* Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).


## 3.3.0 / 2020-05-17 / Agent 7.20.0

***Added***: 

* Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).


## 3.2.1 / 2020-04-04 / Agent 7.19.0

***Fixed***: 

* Update prometheus_client. See [#6200](https://github.com/DataDog/integrations-core/pull/6200).
* Update deprecated imports. See [#6088](https://github.com/DataDog/integrations-core/pull/6088).


## 3.2.0 / 2019-05-14 / Agent 6.12.0

***Added***: 

* Adhere to code style. See [#3560](https://github.com/DataDog/integrations-core/pull/3560).

***Fixed***: 

* Fix type override values in example config. See [#3717](https://github.com/DataDog/integrations-core/pull/3717).


## 3.1.0 / 2019-02-18 / Agent 6.10.0

***Added***: 

* Support Python 3. See [#3048](https://github.com/DataDog/integrations-core/pull/3048).


## 3.0.1 / 2019-01-04 / Agent 6.9.0

***Fixed***: 

* Added crucial words to make sentence clearer. See [#2811][1]. Thanks [someword][2].
* Change the prometheus example to use prometheus_url. See [#2790][3]. Thanks [someword][2].


## 3.0.0 / 2018-10-12 / Agent 6.6.0

***Changed***: 

* Change default prometheus metric limit to 2000. See [#2248][4].

***Fixed***: 

* Temporarily increase the limit of prometheus metrics sent for 6.5. See [#2214][5].


## 2.0.0 / 2018-09-04 / Agent 6.5.0

***Changed***: 

* Bump prometheus client library to 0.3.0. See [#1866][8].

***Added***: 

* Limit Prometheus/OpenMetrics checks to 2000 metrics per run by default. See [#2093][6].
* Make HTTP request timeout configurable in prometheus checks. See [#1790][9].

***Fixed***: 

* Make sure all checks' versions are exposed. See [#1945][7].
* Add data files to the wheel package. See [#1727][10].


## 1.0.0/ 2018-03-23

***Added***: 

* adds prometheus integration.

[1]: https://github.com/DataDog/integrations-core/pull/2811
[2]: https://github.com/someword
[3]: https://github.com/DataDog/integrations-core/pull/2790
[4]: https://github.com/DataDog/integrations-core/pull/2248
[5]: https://github.com/DataDog/integrations-core/pull/2214
[6]: https://github.com/DataDog/integrations-core/pull/2093
[7]: https://github.com/DataDog/integrations-core/pull/1945
[8]: https://github.com/DataDog/integrations-core/pull/1866
[9]: https://github.com/DataDog/integrations-core/pull/1790
[10]: https://github.com/DataDog/integrations-core/pull/1727
