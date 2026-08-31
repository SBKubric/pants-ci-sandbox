module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // Отключить: русский текст и технические термины (HTTP, PostgreSQL)
    // всегда начинаются с заглавной буквы
    'subject-case': [0],
    // Отключить: тех. описания, списки файлов, имена классов/функций
    // легко вылезают за 100 символов в body, перенос их ломает читаемость
    'body-max-line-length': [0],
  },
};
