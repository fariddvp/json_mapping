class JsonKeyValueSwapper:
    def swap_keys_values(self, data):
        if isinstance(data, dict):
            swapped_data = {}
            for key, value in data.items():
                if isinstance(value, list):
                    # اگر مقدار یک لیست باشد، به صورت بازگشتی برای هر آیتم لیست فراخوانی می‌شود
                    swapped_data[key] = [self.swap_keys_values(item) for item in value]
                elif isinstance(value, dict):
                    # اگر مقدار یک دیکشنری باشد، به صورت بازگشتی آن را پردازش می‌کند
                    swapped_data[key] = self.swap_keys_values(value)
                else:
                    # جابجا کردن کلید و مقدار
                    swapped_data[value] = key
            return swapped_data
        elif isinstance(data, list):
            # اگر داده یک لیست باشد، باز هم به صورت بازگشتی برای هر آیتم لیست فراخوانی می‌شود
            return [self.swap_keys_values(item) for item in data]
        else:
            return data  # در غیر این صورت مقدار خودش برگردانده می‌شود (مثلاً برای مقادیر ساده)