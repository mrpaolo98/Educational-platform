# Веб-приложение для онлайн-образования с автоматизированной проверкой знаний
Основное назначение платформы заключается в предоставлении возможности улучшить процесс обучения, автоматизировав процесс проверки знаний и добавив командную работу в процессе обучения.
## Диаграмма вариантов использования
Перед началом разработки нам нужно понять какие действия пользователей нам нужно предусмотреть. Выделим три вида пользователей: Студент, Администратор, Преподаватель. Студент может просмотреть информацию о курсах, посмотреть доступные уроки и их материалы, посмотреть комментарии к нему и оставить свой. Также студент может решить тест, посмотреть результаты тестов и посмотреть командный проект. Администратор может создать направление, объединив тематику курсов, создать курсы в направлениях и предоставлять права доступа Преподавателям и Студентам. Преподаватель может создавать уроки и тесты к ним, курсовые проекты, просматривать курсы и результаты тестирования студентов.
![Диаграмма вариантов использования](https://user-images.githubusercontent.com/59264860/124952273-c5f7f580-e01c-11eb-8502-8426193f5869.jpg)
## Диаграмма базы данных
На данном слайде из сущностей строится схема базы данных. Основными сущностями являются: пользователь, тест, направление курса, занятие, вопрос, командный проект и комментарий. В качестве системы управления базы данных используется MySQL.![Схема базы данных](https://user-images.githubusercontent.com/59264860/124952499-f8a1ee00-e01c-11eb-8fbc-dcb6c0ac7f90.png)
## Граф состояний интерфейса
Граф состояний интерфейса описывает переходы между страницами в процессе обучения пользователем, показывая возможные пути при посещении веб-приложения. Процесс обучения включает в себя следующие основные страницы: регистрация или авторизация пользователя, главная страница и меню, страница курса, урока, курсового проекта, а также страницы тестирования, вопросов и результатов тестирования.![Граф состояний интерфейса](https://user-images.githubusercontent.com/59264860/124952669-1b340700-e01d-11eb-91f0-ee19c92bb2c9.jpg)
## Формы интерфейсов
### Форма регистрации пользователя
![1](https://user-images.githubusercontent.com/59264860/124952853-3f8fe380-e01d-11eb-92ed-6be847a053a0.jpg)
### Страница урока и его материалов
![2](https://user-images.githubusercontent.com/59264860/124952909-4e769600-e01d-11eb-838e-f0d75590736f.jpg)
### Вопросы при тестировании
![3](https://user-images.githubusercontent.com/59264860/124952968-5e8e7580-e01d-11eb-8660-62fd4718f858.jpg)
### Результаты тестирования
![4](https://user-images.githubusercontent.com/59264860/124953032-70701880-e01d-11eb-84fa-e630aafcf80e.jpg)