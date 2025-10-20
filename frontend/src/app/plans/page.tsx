
export default function PlansPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center">
      <h1 className="text-3xl font-bold">پلن‌های اشتراک</h1>
      <p className="mt-4 text-lg">
        به زودی پلن‌های مختلف در این صفحه نمایش داده خواهند شد.
      </p>
      {/* Placeholder for plan cards */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="border p-6 rounded-lg">
          <h2 className="text-2xl font-semibold">آزمایشی</h2>
          <p className="mt-2">ویژگی‌های پلن آزمایشی...</p>
        </div>
        <div className="border p-6 rounded-lg">
          <h2 className="text-2xl font-semibold">پایه</h2>
          <p className="mt-2">ویژگی‌های پلن پایه...</p>
        </div>
        <div className="border p-6 rounded-lg">
          <h2 className="text-2xl font-semibold">حرفه‌ای</h2>
          <p className="mt-2">ویژگی‌های پلن حرفه‌ای...</p>
        </div>
      </div>
    </div>
  );
}
