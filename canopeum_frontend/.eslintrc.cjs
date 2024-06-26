/** @type {import("eslint").Linter.Config} */
module.exports = {
  root: true,
  extends: [
    'beslogic/react',
    'beslogic/typescript',
    'beslogic/dprint',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: ['tsconfig?(.*).json'],
  },
  ignorePatterns: [
    '.eslintrc.cjs',
    // Auto-generated
    'src/services/api.ts',
  ],
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
    /*
     * Beslogic presets overrides
     */
    // For now, we're fine using relative paths instead of ts-paths in this project
    'no-autofix/no-relative-import-paths/no-relative-import-paths': 'off',
    // Using Bootraps directly without a React wrapper will cause us to have to add classes to React Components
    'react/forbid-component-props': 'off',
    '@typescript-eslint/no-unsafe-member-access': 'warn',
  },
}
