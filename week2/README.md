# Week 2

We walked through the app code here:

https://github.com/StudentDevs/app/tree/week2

The app implements user account creation, login, logout,
and a quiz using an unofficial API of SpaceX data.

Opening and merging a pull request demonstrated here:

https://github.com/StudentDevs/app/pull/1

## Development project over the next week

Add a database table where you store each submitted answer along with the
question details. For example, maybe your table would have these fields:
`account_id`, `user_answer`, `correct_answer`, `title`, `details`.
Then, once you’re storing those, display on the user’s home page
(the path `/` when logged in) their history of answered questions so they
can see which and how many they’ve gotten correct or wrong.
